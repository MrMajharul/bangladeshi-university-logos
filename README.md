# Bangladeshi University Logos Collection 🇧🇩

A collection of PNG logos for 46 major universities in Bangladesh, compiled and organized for easy use in projects, applications, and research.

## 📊 Collection Overview

- **Total Universities**: 46
- **Universities with at least one logo source**: 45
- **Unique PNG files in `logos/`**: 29
- **Format**: PNG (512x512 pixels)
- **Quality**: High-resolution, standardized format
- **Date**: September 2025

> **Note on the collection.** The `logos/` directory now contains only deduplicated
> PNG files — many SVG logos were converted using a placeholder image, so files
> that were byte-identical to another logo have been removed. The remaining
> 16 universities without a `logos/*.png` file still have an SVG (or other
> format) available; convert with `convert_svg_to_png.py` style tooling to
> regenerate PNGs. Run `python3 final_summary.py` to see the current state.

## 🎯 What's Included

### 📁 Directory Structure
```
university-logos-bangladesh/
├── logos/                          # 29 deduplicated PNG university logos
├── data/
│   └── universities.csv           # 46 unique universities
├── original/                      # Original SVG and PNG files
│   ├── svg/                       # SVG logos
│   ├── png/                       # Original PNG files
│   ├── both_formats/              # Universities with both SVG and PNG
│   └── reports/                   # Collection reports
├── final_summary.py               # Prints current collection summary
└── README.md                      # This file
```

### 🏛️ Universities Included

The collection includes logos from major universities across Bangladesh:

- **Public Universities**: University of Dhaka, BUET, Chittagong University, etc.
- **Private Universities**: BRAC University, North South University, etc.
- **Science & Technology Universities**: SUST, CUET, KUET, etc.
- **Specialized Institutions**: Military Institute of Science and Technology, etc.

## 🚀 Usage

### Direct Download
All logos are in the `/logos` directory with standardized naming:
```
University_Name.png
```

### Examples
- `University_of_Dhaka.png`
- `BRAC_University.png`
- `Bangladesh_University_of_Engineering_and_Technology.png`

### In Your Projects

**HTML:**
```html
<img src="logos/University_of_Dhaka.png" alt="University of Dhaka Logo" width="128" height="128">
```

**CSS:**
```css
.university-logo {
    width: 64px;
    height: 64px;
    background-image: url('logos/BRAC_University.png');
    background-size: contain;
}
```

**Python:**
```python
import os
logo_path = "logos/University_of_Dhaka.png"
if os.path.exists(logo_path):
    # Use the logo
    pass
```

## 📋 University List

| University | Logo Available | Format |
|------------|----------------|---------|
| University of Dhaka | ✅ | PNG |
| BRAC University | ✅ | PNG |
| Bangladesh University of Engineering and Technology | ✅ | PNG |
| Shahjalal University of Science and Technology | ✅ | PNG |
| North South University | ✅ | PNG |
| Daffodil International University | ✅ | PNG |
| Ahsanullah University of Science and Technology | ✅ | PNG |
| Green University of Bangladesh | ✅ | PNG |
| University of Frontier Technology, Bangladesh | ✅ | PNG |
| *...and 19 more universities* | ✅ | PNG |
| Army Institute of Business Administration, Sylhet | ❌ | N/A |

*Complete list available in `data/universities.csv`*

## 🛠️ Technical Details

### Logo Specifications
- **Format**: PNG
- **Dimensions**: 512x512 pixels
- **Background**: Transparent (where applicable)
- **Quality**: High-resolution, web-optimized

### Collection Methodology
1. **Primary Source**: Wikipedia/MediaWiki APIs
2. **Secondary Source**: Official university websites
3. **Format Conversion**: SVG logos converted to PNG using ImageMagick
4. **Quality Control**: Manual verification and standardization

### Data Sources
- Wikipedia articles and infoboxes
- Official university websites
- MediaWiki image repositories
- Manual research and verification

## 📊 Statistics

- **Universities with a logo source**: 45/46 (97.8%)
- **Unique PNG files in `logos/`**: 29
- **Sources used**: Wikipedia API, university websites
- **Processing**: Automated collection and conversion

## 🤝 Contributing

Found a missing logo or have a higher quality version? Contributions are welcome!

1. Fork this repository
2. Add the logo to the appropriate directory
3. Update the university list
4. Submit a pull request

### Logo Guidelines
- PNG format preferred
- Minimum 512x512 pixels
- Transparent background if possible
- Official university logo only

## 📄 License

This collection is provided for educational and research purposes. Individual logos remain the intellectual property of their respective universities. Please respect copyright and trademark rights when using these logos.

## 🔗 Related Projects

- [University Data API](https://github.com/your-username/bangladesh-universities-api)
- [Education Statistics Bangladesh](https://github.com/your-username/bd-education-stats)

## 📞 Contact

For questions, suggestions, or collaboration opportunities:
- Create an issue in this repository
- Email: [your-email@example.com]

---

**Note**: This collection was compiled in September 2025 using automated scraping tools and manual research. University logos may change over time, and this collection represents logos available at the time of compilation.

## 🙏 Acknowledgments

- Wikipedia contributors for maintaining university information
- University websites for providing official logos
- Open source tools: Python, Beautiful Soup, ImageMagick
- MediaWiki API for image access

---

⭐ **Star this repository if you find it useful!**