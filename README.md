## About
- Oxford University Digital Innovation Team showcases VR in its Immersive Lab and loan equipment
- This web app curates a selection of commercially available VR apps for Meta Quest 2 and 3 VR Headsets
- It is designed to be bookmarked and used in the Meta Quest browser, as well as desktop browsers
- The curation is work in progress and an ongoing activity of discovery and optimisation

## App Usage
- The VR apps are curated into a set of categories relevant to Oxford University
- VR pointer or PC mouse-over of an app card gives tool tip information about each VR app
- Clicking an app card opens new tab to the meta experience page or webXR link

## App Design
- Web app reads bookmarks.json to render
- Includes logic to override data caching
- links at bottom of page to book visit (MS Bookings) and to suggest an app (MS Forms)
- The VR apps data is maintained as a CSV file, openend in Excel (for simple editting by non technical staff)
- Utility provided to convert CSV to JSON, also adds metadata (date, title)

## Known Issues
- touch screen user interaction e.g. from a mobile or tablet does not work well for tool tips  

## Deployment
- web app deployment files in /docs folder
- published on github-pages: https://ox-dig-innov.github.io/curated-vr-apps/

## Utils
- Tools to convert from CSV or Excel to JSON
- The Web app is recommended as the most simple to use

### Web app
- web app to convert VR Bookmarks from CSV or Excel to JSON
- input: **bookmarks.csv** or **bookmarks.xlsx** - master file used for manual editing the data
- output: **bookmarks.json** - used by main app
- tool adds current date and a title to output file
- selects specific columns from input, defined as INCLUDE_COLUMNS
- ignores any extra columns, so can store metadata which is not transferred to output
- web app deployed to https://ox-dig-innov.github.io/curated-vr-apps/update


#### Usage
1. Open https://ox-dig-innov.github.io/curated-vr-apps/update
2. Drag updated CSV/XLS data file into the app (or file pick)
3. Download the resulting **bookmarks.json** file
4. Manually deploy **bookmarks.json** file in /data folder


#### Configuration
```
const ABOUT_TITLE = "Digital Innovation Curated VR Apps";
const INCLUDE_COLUMNS = ["title", "url", "about"];

```



### Python tool (legacy)
#### convert-to-json.py
- Command Line tool to convert VR Bookmarks from CSV to JSON
- tool adds current date and a title to JSON
- selects specific columns in CSV, defined as REQUIRED_COLUMNS
- ignores any extra columns in CSV, so CSV can store metadata which is not transferred to JSON
- input: CSV - master file used for manual editing the data
- output: JSON - used by main app

#### Usage
`python convert-to-json.py bookmarks.csv bookmarks.json`

#### Configuration
```
# Constants
ABOUT_TITLE = "Digital Innovation Curated VR Apps"
DATE_FORMAT = "%d %b %Y"
REQUIRED_COLUMNS = ['group', 'title', 'url', 'about']
```


## Data file formats

#### CSV Format



#### JSON Format
```
{
  "about": {
    "title": "Digital Innovation Curated VR Apps",
    "created": "25 Feb 2025"
  },
  "groups": [
    {
      "group": "Wellbeing",
      "bookmarks": [
        {
          "title": "Flowborne VR",
          "url": "https://www.meta.com/en-gb/experiences/4997438576996478/",
          "about": "A meditative breathwork experience enhanced by biofeedback to cultivate a peaceful and serene breathing style. Created by psychologists, it seeks to help alleviate stress and promote deep relaxation. Embark on a soothing journey through enchanting worlds, release tension, and master the art of diaphragmatic breathing. Your very own breath powers the experience as the VR controller captures your abdomen movements. The virtual environment responds to your breathing in real time, guiding your focus and helping you perfect your breathing style. Each exhale translates into a floating movement, allowing for serene exploration within the virtual realm."
        },
        {
          "title": "Nature Treks VR",
          "url": "https://www.meta.com/en-gb/experiences/2616537008386430",
          "about": "Explore tropical beaches, underwater oceans and even take to the stars. Discover over 20 different animals, command the weather, take control of the night or shape your own world with ‘orbs’, breathe with the meditation lotus. Immerse yourself into the Nature Treks VR experience and escape into a world of relaxation."
        },
        {....
```

