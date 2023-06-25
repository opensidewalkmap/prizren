"""
  setup the variables for your city:

  all of them are mandatory!!
"""

# Full city name, it may contain special characters, spaces...
CITY_NAME = 'Prizren'

# simple name, spaces must be replaced by underscores, no special characters, all in lowercase
CITY_SHORTNAME = 'prizren'

# username, for adresses
USERNAME = 'opensidewalkmap'

# repository name, for many weblink references:
REPO_NAME = 'prizren'

# City OSM relation id: (search at  https://nominatim.openstreetmap.org/ui/search.html ):
CITY_RELATION_ID = 'N150906142' #as string!!

# BOUNDING BOXES
# A good tool to find them is: bboxfinder.com
# # entire city: 
BOUNDING_BOX = (20.678329,42.179434,20.802269,42.248089)

# # A sample of a region of special interest, like the city centre, 
# # It must have sidewalks as geometries and be inside the bigger one!!
BOUNDING_BOX_SAMPLE = (20.699401,42.226960,20.727832,42.237383)

STREAMLIT_URL='https://kauevestena-opensidewalkmap-beta-streamlit-routing-app-52bins.streamlitapp.com/'
