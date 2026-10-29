# Asian-sourced alternatives to Charles River Endosafe LAL cartridges

Research date: 2026-10-29

## Target product

Charles River Endosafe kinetic chromogenic LAL cartridges (nexgen-PTS / nexgen-MCS readers).
Single-use, 4-channel cartridge (2 sample channels + 2 positive-product-control channels),
25 uL sample per channel, result in about 15 minutes, sensitivities of 0.005 / 0.01 / 0.05 / 0.1 EU/mL,
FDA-licensed LAL for release testing (unlicensed versions exist for non-release use).
Charles River also sells Trillium rCR (recombinant cascade reagent) cartridges for the same readers.

## Bottom line

1. There is no third-party cartridge that fits the nexgen-PTS / MCS. The cartridge is proprietary
   and patented, and Charles River states no other brand of reader uses cartridge technology.
   The only "domestic" Chinese listing found (Beijing Hengyi Deke, "portable bacterial endotoxin
   analyzer") reuses Endosafe marketing text and appears to be a reseller or grey-market listing,
   not a Chinese-made cartridge.
2. A replacement therefore means changing platform. The options below are ranked by how closely
   they reproduce the cartridge workflow (point-of-use, pre-dispensed reagent, small sample, fast result).

## Option 1: CMD aBET system with FUJIFILM Wako PYROSTAR ES-F (closest functional match)

- Reader + single-use 4-channel cartridges, portable, fully integrated. Consumables pack: 25 cartridges
  plus 5 vials of nanorod reagent = 100 assays.
- Reagent: PYROSTAR ES-F, an FDA-licensed, endotoxin-specific LAL from FUJIFILM Wako (Japan).
  The LAL line is now sold under FUJIFILM Biosciences (since Oct 2024).
- Range 0.001 to 10 EU/mL from a single reagent. Time to result depends on concentration:
  about 3 min at 10 EU/mL, under 11 min at 0.1 EU/mL, up to 30 min at 0.001 EU/mL.
- Caveats: the instrument and cartridge are made by Cotton Mouton Diagnostics (UK), so only the
  reagent is Asian-sourced. The chemistry is kinetic turbidimetric, not kinetic chromogenic, so the
  USP <85> method changes and product-specific interference testing must be repeated.

## Option 2: FUJIFILM Wako single-test vials on the Toxinometer ET-7000 (Japan)

- Limulus Color KY Single Test: kinetic chromogenic, pre-dispensed single-test vials,
  0.0002 to 0.5 EU/mL on the ET-7000.
- PYROSTAR ES-F Single Test: kinetic turbidimetric, 0.001 to 10 EU/mL, 0.2 mL sample per vial.
- Toxinometer ET-7000: benchtop incubating tube reader, 16 wells per module, up to 8 modules (128 tests),
  21 CFR Part 11 set available. Not handheld, but compact and single-test friendly.
- Same kinetic chromogenic principle as the Endosafe cartridge, so the compendial method stays the same.
  Sample volume is larger (200 uL vs 25 uL) and a standard curve is run per batch rather than stored in
  the cartridge.

## Option 3: Chinese TAL kinetic chromogenic kits on an incubating microplate reader (lowest cost)

All use Tachypleus amebocyte lysate (TAL) co-lyophilized with chromogenic substrate, read at 405 nm
on an incubating kinetic plate reader (for example BioTek ELx808) with the vendor's software.

| Vendor | Product | Range | Notes |
|---|---|---|---|
| Xiamen Bioendo Technology | Micro KC Endotoxin Test Kit (MKC0505 series) | 0.005 to 5 or 0.01 to 10 EU/mL | 25 uL sample + 25 uL lysate per well, 90 tests, detachable 8-well strips; also sells KC kits, rFC fluorometric kit, reader and software; active exporter |
| Xiamen Houshiji (Chinese Horseshoe Crab Reagent Manufactory) | Kinetic chromogenic TAL kit | not published in English | First SFDA-licensed TAL maker in China (1980); Chinese-language catalogue |
| Zhanjiang Bokang Marine Biological (export via Accumedi Solutions) | TAL kits incl. kinetic chromogenic | not published in English | Oldest Chinese TAL maker (1986), top-3 by volume |
| Fuzhou Xinbei Biochemical | TAL kits incl. chromogenic | not published in English | Exhibits at AACC; mainly pharma and clinical TAL |

Note: Zhanjiang A&C Biological, another TAL maker, is a division of Charles River, so it is not an
independent source.

Caveats: these reagents are registered against the Chinese Pharmacopoeia. None of the vendors shows
an FDA LAL license or NMPA device registration in English-language material. For US release testing
an FDA-licensed reagent is expected, so these fit best for in-process, water, and non-US markets, or
after a full USP <85> / EP 2.6.14 validation. Per-test cost is far lower than cartridges, but throughput
comes from 96-well batches, not single tests.

## Option 4: Asian recombinant (animal-free) reagents, analogous to the Trillium rCR cartridge

- FUJIFILM Wako PYROSTAR Neo+ (Japan, launched July 2024): recombinant Factor C + Factor B + proclotting
  enzyme cascade, kinetic chromogenic, 0.001 to 50 EU/mL. Plate or tube reader format.
- ACROBiosystems SAFENSURE rFC kit (China HQ, offices in Korea and elsewhere): 0.005 to 5 EU/mL,
  fluorometric, about 1 hour, 48 or 96 tests; validated with Tecan readers.
- Xiamen Bioendo rFC Endotoxin Test Kit: fluorometric, 0.005 EU/mL lower limit.
- All plate-based; use USP <86> / EP 2.6.32 for recombinant reagents.

## Recommendation

- Keep the point-of-use cartridge workflow: evaluate the CMD aBET with PYROSTAR ES-F (Japanese reagent).
- Keep kinetic chromogenic and FDA-licensed reagent, but accept a benchtop reader: Wako Limulus Color KY
  single-test vials on the Toxinometer ET-7000.
- Lowest cost, Asian-made, plate reader acceptable: Xiamen Bioendo Micro KC kit (same 25 uL sample volume
  as the cartridge). Request IFU, CoA, registration certificates, and a lot-to-lot stability summary first.
- Animal-free: PYROSTAR Neo+.

## Next steps before any switch

1. Get quotes with cost per reportable result (include PPC, standards, plates, reader amortization).
2. Ask each vendor for regulatory status: FDA LAL license (US), NMPA registration (China), CE/IVDR,
   and whether the reagent is listed in a pharmacopoeia monograph.
3. Run USP <85> method suitability (interference / PPC recovery) on your actual products.
4. Confirm reader software supports 21 CFR Part 11 if used for release.

## Sources

- Charles River cartridge and nexgen-PTS pages (criver.com), Fisher Scientific listings NC9594798 / NC9118809
- rapidmicrobiology.com: Endosafe nexgen-PTS; aBET launch (Dec 2022); CMD aBET consumables pack (Jan 2024)
- cm-dx.com/alphabet; wakopyrostar.com (aBET, Toxinometer, Limulus Color KY, PYROSTAR ES-F); Avantor/VWR listings
- fujifilm.com news: PYROSTAR Neo+ and LumiMAT launch (June 2024)
- bioendo.com product pages (Micro KC, KC, rFC kits); gaiascience.com.sg Micro KC listing
- houshiji.com product pages; freshdi.com supplier profile; bionity.com Accumedi/Bokang profile
- newswise.com: Fuzhou Xinbei at AACC 2018
- kr.acrobiosystems.com SAFENSURE rFC kit
- horseshoecrab.org manufacturer list (Zhanjiang A&C as Charles River division)
- criver-microbial.cn (Charles River China) and ybzhan.cn Beijing Hengyi Deke listing
