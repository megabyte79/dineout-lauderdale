"""Derived fields for payload.json.

Every entry stores a few values that are computed from its menu rather than
scraped: what the best and worst combinations come to, the resulting verdict,
and a confidence rollup. This module is the single definition of those rules.

Run it directly to recompute the whole payload in place:

    python3 recompute.py            # rewrite payload.json
    python3 recompute.py --check    # verify stored values, change nothing
"""
import json
import sys

PAYLOAD = 'payload.json'

# A dish's price confidence, set during research:
#   HIGH  exact match on the restaurant's current published menu
#   MED   close match, a renamed dish, or a reliable secondary source
#   LOW   no published price anywhere; benchmarked estimate
DERIVED = ('pick', 'picks', 'best', 'worst', 'median', 'spread', 'pct', 'pctbest',
           'verdict', 'n', 'low', 'high', 'confidence', 'courses_n')

# How close to the tier price counts as neither a deal nor a rip-off. A menu
# whose best combination lands 11 cents under what you pay is a wash, not a
# warning, and a la carte prices move by more than that between visits.
EVEN_BAND = 0.03


def net(o):
    """What a dish is worth *toward the base price*.

    A dish carrying a supplement costs extra on top of the prix fixe, so only
    the difference counts. A $54 ribeye at +$15 contributes $39 of value
    against the base price. This is the same arithmetic as comparing the meal
    against (tier + supplement), just expressed per dish so the rest of the
    scoring is unchanged.
    """
    return o['price'] - (o.get('supp') or 0)


def verdict_of(tier, best, worst, party_unclear=False):
    """How the prix fixe compares to ordering the same dishes a la carte.

    tier  is what you pay; best/worst are the priciest and cheapest
    combinations you could order off the prix fixe menu.
    """
    if tier == 0:
        return 'nomenu'      # restaurant published no menu for this tier
    if party_unclear:
        return 'party'       # tier is priced for a party; per-person value is unknowable
    if abs(best - tier) <= tier * EVEN_BAND:
        return 'even'        # best case lands on the price either way; a wash
    if best < tier:
        return 'skip'        # even ordering the most expensive option loses
    if worst >= tier:
        return 'safe'        # every combination beats the price
    if best >= tier * 1.15:
        return 'pick'        # worth it if you order well
    return 'marginal'        # close either way


def recompute(e):
    """Refresh every derived field on one entry, in place.

    Entries whose restaurant never published a menu carry no priced items at
    all; they are marked 'nomenu' and their numeric fields are left alone.
    """
    menu = e['menu']
    if not any(menu.values()) and not (e.get('included') or []):
        e['verdict'] = 'nomenu'
        e['confidence'] = 'none'
        e['n'] = e['low'] = e['high'] = 0
        return e

    for course in menu:
        menu[course].sort(key=lambda o: -net(o))

    # Most courses are "choose one", but a few tiers hand the table a list and
    # say "select two". `choose` records that; it defaults to one per course.
    choose = e.get('choose') or {}

    # The best-value option(s) in each course, after netting out any supplement.
    e['picks'] = {c: opts[:min(choose.get(c, 1), len(opts))]
                  for c, opts in menu.items() if opts}
    e['pick'] = {c: opts[0] for c, opts in e['picks'].items()}
    best = sum(net(o) for opts in e['picks'].values() for o in opts)
    worst = sum(sum(net(o) for o in opts[-min(choose.get(c, 1), len(opts)):])
                for c, opts in menu.items() if opts)

    # Items that come with the meal rather than being chosen between.
    # 'choose' means the guest picks one of them; anything else means all are served.
    included = e.get('included') or []
    if included:
        if e.get('included_mode') == 'choose':
            best += max(o['price'] for o in included)
            worst += min(o['price'] for o in included)
        else:
            total = sum(o['price'] for o in included)
            best += total
            worst += total

    # A tier headed "Dinner for Two" buys that many full menus for one price,
    # so the food on the table is worth that many times one guest's picks.
    # Scoring one guest's worth against a two-guest price is what produced a
    # false "costs more" on Bodega's $60 menu.
    covers = e.get('covers') or 1
    best *= covers
    worst *= covers

    tier = e['tier']
    e['best'] = round(best, 2)
    e['worst'] = round(worst, 2)
    e['median'] = round((best + worst) / 2, 2)
    e['spread'] = round(best - worst, 2)
    e['pct'] = round((e['median'] - tier) / tier * 100, 1) if tier else 0
    e['pctbest'] = round((best - tier) / tier * 100, 1) if tier else 0
    e['verdict'] = verdict_of(tier, best, worst, bool(e.get('party_unclear')))

    confs = ([o['conf'] for opts in menu.values() for o in opts]
             + [o['conf'] for o in included])
    e['n'] = len(confs)
    e['low'] = sum(1 for c in confs if c == 'LOW')
    e['high'] = sum(1 for c in confs if c == 'HIGH')
    # verified: every price came off a current menu. estimated: none did.
    e['confidence'] = ('verified' if e['low'] == 0 else
                       'estimated' if e['high'] == 0 else 'mixed')
    e['courses_n'] = len([c for c in menu if menu[c]])
    return e


def main():
    check = '--check' in sys.argv
    payload = json.load(open(PAYLOAD))

    stale = []
    for entry in payload:
        before = {k: entry.get(k) for k in DERIVED}
        recompute(entry)
        for field in DERIVED:
            # 'nomenu' entries only have verdict/confidence/counts derived
            if field not in entry:
                continue
            if before[field] != entry[field]:
                stale.append((entry['restaurant'], entry['meal'], field,
                              before[field], entry[field]))

    if check:
        if stale:
            print(f'{len(stale)} stored value(s) disagree with the rules:')
            for r, m, f, was, now in stale:
                print(f'  {r} [{m}] {f}: stored={was!r} computed={now!r}')
            return 1
        print(f'OK: all derived fields on {len(payload)} entries match the rules.')
        return 0

    json.dump(payload, open(PAYLOAD, 'w'), ensure_ascii=False)
    print(f'Recomputed {len(payload)} entries ({len(stale)} field(s) updated).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
