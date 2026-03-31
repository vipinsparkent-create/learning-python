import webbrowser
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My First Python Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f8ff;
            padding: 60px;
        }
        h1 { color: #2c3e50; }
        p  { color: #555; font-size: 18px; }
        .box {
            background: white;
            border-radius: 12px;
            padding: 40px;
            display: inline-block;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>Hello! This is Vipin </h1>
        <p>This page was created by my Python program.</p>
        <p>Today I wrote my first web output! - mark this date 1st April 2026</p>
    </div>
</body>
</html>
"""

filename = "my_first_page.html"
with open(filename, "w") as f:
    f.write(html_content)

webbrowser.open("file://" + os.path.abspath(filename))
print("Done! Your page should open in the browser.")