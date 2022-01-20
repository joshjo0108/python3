# DICTIONARY
courses = {
    "js": "Javascript 101",
    "python": ["Python101", "Python201"],
    "html": "HTML 101"
}

# DEFAULT as None, IF THERE IS NOTHING IN AS VALUE
print(courses.get("js", None))  
print(courses.get("KEY", None)) # THIS IS SET DEFAULT AS None

# None == False
# IF css EXISTS print(), ELSE JUST SKIP IT
if courses.get("css", None):
    print("You are enrolled in CSS 101")