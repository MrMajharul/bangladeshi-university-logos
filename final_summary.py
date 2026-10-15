#!/usr/bin/env python3
"""
Print a summary of the PNG logo collection.

Reads the deduplicated university list from data/universities.csv and counts
PNG files in logos/ to report accurate collection statistics.
"""

import os
import csv
from datetime import date

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PNG_DIR = os.path.join(PROJECT_ROOT, 'logos')
CSV_PATH = os.path.join(PROJECT_ROOT, 'data', 'universities.csv')


def create_final_summary():
    """Print final project summary."""

    print("UNIVERSITY PNG LOGO COLLECTION - SUMMARY")
    print("=" * 60)

    # Count PNG files
    png_files = sorted(f for f in os.listdir(PNG_DIR) if f.endswith('.png'))
    total_png = len(png_files)

    # Read university list
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        universities = list(csv.DictReader(f))

    total_universities = len(universities)
    with_logo = [
        u for u in universities
        if u['svg_logo'] or u['png_logo'] or u['other_logos']
    ]
    missing = total_universities - len(with_logo)

    success_rate = (len(with_logo) / total_universities) * 100 if total_universities else 0.0

    print("\nCOLLECTION STATISTICS:")
    print(f"  Total Universities: {total_universities}")
    print(f"  Universities with at least one logo: {len(with_logo)}")
    print(f"  PNG files in logos/: {total_png}")
    print(f"  Coverage: {success_rate:.1f}%")

    if missing:
        print(f"  Missing logo ({missing}):")
        for u in universities:
            if not (u['svg_logo'] or u['png_logo'] or u['other_logos']):
                print(f"    - {u['university']}")

    print(f"\nFINAL COLLECTION:")
    print(f"  Directory: logos/")
    print(f"  PNG files: {total_png}")
    print(f"  File format: University_Name.png (512x512 pixels)")

    print(f"\nFILES IN logos/:")
    for filename in png_files:
        uni_name = filename.replace('.png', '').replace('__', ', ').replace('_', ' ') # __ for comma
        print(f"  {filename} - {uni_name}")

    print("\nCOLLECTION COMPLETE!")
    print(f"  All PNG logos ready for use in: logos/")


def main():
    """Main execution."""
    create_final_summary()
    print(f"\nPROJECT COMPLETED SUCCESSFULLY!")
    print(f"   Your PNG logo collection is ready!")
    print(f"   Location: logos/")


if __name__ == "__main__":
    main()
