# Dine Out Lauderdale 2026, decoded

An unofficial value guide to [Dine Out Lauderdale](https://www.visitlauderdale.com/dineout)
(August 1 to September 30, 2026). It prices every prix fixe dish against what the
same dish costs off the restaurant's regular menu, so you can tell which fixed
price meals are actually a deal and which ones are not.

**Live site:** https://megabyte79.github.io/dineout-lauderdale/

## Heads up: `index.html` is generated

`index.html` is a build artifact, not something to edit. It is one self contained
file with the data inlined, which is why it is close to a megabyte and why one
line in it is very long. If you came here from the live site and opened that file
first, that is the confusing part. The actual source is small:

| File | What it is |
|---|---|
| `payload.json` | The data. One entry per restaurant *and* meal tier, so a place doing both lunch and dinner has two entries. |
| `build_page.py` | The generator. Reads `payload.json`, writes the page. |
| `recompute.py` | The scoring rules (best/worst/verdict/confidence). Also a checker. |
| `report.html` | The "spot an error" page. Posts into a Google Form, no account needed. |
| `index.html` | Generated output. Do not edit by hand. |

## Building

```sh
python3 build_page.py          # writes dineout_guide.html
cp dineout_guide.html index.html
```

No dependencies, Python 3 standard library only. `recompute.py` needs to run
first if you have edited any prices:

```sh
python3 recompute.py           # refresh derived fields in payload.json
python3 recompute.py --check   # verify stored values match the rules, change nothing
```

`--check` exits non-zero if anything has drifted. It is worth running before a
commit; it has already caught confidence badges that were stale after hand edits.

## How the value number works

Each course lists several options at different everyday prices, so a prix fixe
menu does not have one value, it has a range. A dish that carries a supplement
(say +$12 on top of the fixed price) only counts for its price minus the
supplement, since that is what it is worth *toward* the base price:

- **best** is the sum of the highest net-value option in each course
- **worst** is the sum of the lowest

A course that hands you two picks sums two, and a tier priced for two people
(Bodega's $60 "Dinner for Two") counts two full menus. Both are compared
against **tier**, the advertised price. That produces the verdict:

| Verdict | Rule | Meaning |
|---|---|---|
| `safe` | `worst >= tier` | Every combination beats the price |
| `pick` | `best >= tier * 1.15` | Worth it if you order well |
| `marginal` | otherwise | Close either way |
| `even` | `best` within 3% of `tier` | At best you break even, so go for the food, not the discount |
| `skip` | `best < tier` | Even the priciest order loses |
| `party` | listing says "for 2" but not what that buys | Shown, but not scored, guessing would publish a coin flip |
| `nomenu` | no menu published | Nothing to score |

Prices are portion adjusted. A 4 piece appetizer on the prix fixe is priced
against a 4 piece share of the restaurant's regular 8 piece order, not the whole
thing. Figures are before tax and tip. Genuinely included drinks and sides are
counted. An upgrade whose regular price is unknown (the listing gives only the
upcharge) is shown on the card but left out of the math entirely.

### Two things that are easy to get wrong

The visitlauderdale listing template has a free form fourth block called
"Special Offerings" that restaurants use for completely different purposes. Some
put an alternative main in it, some put included drinks, some put paid upcharges.
Counting it uniformly as a bonus course inflates the total. Each one in this data
set was checked against its listing individually.

Some restaurants serve a family style tasting where you get every dish rather
than choosing one. Those use `"included_mode": "all"`. Reading one as choose-one
badly understates it.

## Price confidence

Every dish carries a `conf` value, surfaced on each card so you know how much to
trust it:

- `HIGH` exact match on the restaurant's current published menu
- `MED` close match, a renamed dish, or a reliable secondary source
- `LOW` no published price anywhere, benchmarked estimate

Rolled up per menu: **verified** (no LOW prices), **estimated** (no HIGH prices),
**mixed** (some of each). Each dish also stores the source it came from, shown
under the dish on the card.

## Spot an error?

Every card links to [the report page](https://megabyte79.github.io/dineout-lauderdale/report.html),
which takes thirty seconds and needs no account. Upcharges that only appear at
the table are invisible to any menu research, so readers are the only way those
ever get found. The full history of corrections is in the
[commit log](https://github.com/megabyte79/dineout-lauderdale/commits/main).

## Caveats

Menus were captured from visitlauderdale.com in August 2026. Restaurants change
menus and prices without notice, and some publish no prices at all, in which case
the numbers here are benchmarked estimates that are useful for ranking and not
worth arguing over. Always call ahead. This is a hobby project and is not
affiliated with Visit Lauderdale.
