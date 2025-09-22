# Bangladeshi University Logos Collection 🇧🇩

A comprehensive collection of PNG logos for 50 major universities in Bangladesh, compiled and organized for easy use in projects, applications, and research.

## 📊 Collection Overview

- **Total Universities**: 50
- **Logos Collected**: 49 (98% success rate)
- **Format**: PNG (512x512 pixels)
- **Quality**: High-resolution, standardized format
- **Date**: September 2025

## 🎯 What's Included

### 📁 Directory Structure
```
university-logos-bangladesh/
├── logos/                          # 49 PNG university logos
├── data/
│   └── universities.csv           # Complete university database
├── original/                      # Original SVG and PNG files
│   ├── svg/                      # 44 SVG logos
│   └── png/                      # 22 original PNG files
└── README.md                     # This file
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
| Chittagong University of Engineering and Technology | ✅ | PNG |
| North South University | ✅ | PNG |
| East West University | ✅ | PNG |
| American International University-Bangladesh | ✅ | PNG |
| Daffodil International University | ✅ | PNG |
| Independent University, Bangladesh | ✅ | PNG |
| *...and 39 more universities* | ✅ | PNG |
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

- **Success Rate**: 98% (49/50 universities)
- **Original PNG Files**: 39 universities
- **SVG Converted to PNG**: 10 universities
- **Sources Used**: Wikipedia API, university websites
- **Processing Time**: Automated collection and conversion

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