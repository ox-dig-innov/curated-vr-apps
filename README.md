## About
- Web app to display Digital Innovation Team's curated VR apps for Meta Quest 2 and 3.
- Can be bookmarked and browsed in Quest headset, as well as desktop browser
- apps are curated into categores
- mouse over or point to an app card gives information about the app
- clicking opens new tab to the meta experience page or webXR link

## App Design
- Web app reads bookmarks.json to render
- Includes logic to overide data caching
- links at bottom of page to book visit (MS Bookings) and to suggest an app (MS Forms)
- Bookmarks data is maintained and updated in Excel as a CSV file
- Utility provided to convert CSV to JSON, also adds metadata (date, title)



## Utils
#### convert-to-json.py
- Command Line tool to convert VR Bookmarks from CSV to JSON
- tool adds current date and a title to JSON
- selects specific columns in CSV, defined as REQUIRED_COLUMNS
- ignores any extra columns in CSV, so CSV can store metadata which is not transferred to JSON
- input: CSV - master file used for manual editing the data
- output: JSON - used by web app


#### Usage
`python convert-to-json.py bookmarks.csv bookmarks.json`

#### Configuration
```
# Constants
ABOUT_TITLE = "Digital Innovation Curated VR Apps"
DATE_FORMAT = "%d %b %Y"
REQUIRED_COLUMNS = ['name', 'title', 'url', 'about']
```



#### JSON Format
```
{
  "about": {
    "title": "Digital Innovation Curated VR Apps",
    "created": "03 Feb 2025"
  },
  "groups": [
    {
      "name": "Wellbeing",
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

