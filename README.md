# Online Book to pdf 
### Purpose:
Certain websites allow users to read books online but prohibit their downloading. The disadvantage of those websites is that
they are not available under offline mode. To compensate for this, I came up with an idea to develop a script that would
allow one to download an online book in the pdf format.

![alt text](https://lh3.googleusercontent.com/proxy/hoDhkyw5FlP7K5Z9gu-w-yzWJ5yr-6-IRgYvJUZfz0hFzRS3PaqRy7USCiosuO1P6dzFjIupLH_WK1JBpitZTtTd3qSxZ7kODIGtkVKiTy23b5HFSI9GTpnYnYiH9ig8vVumVil-YLq0r9qwHbtbVQ)

### About Script:
The script was made to allow copying online books and converting them into pdf format. To use the script, a user needs to give
coordinates of the screenshot region and the "next page" button.

### Usage:
The script mouse.py returns your mouse’s coordinates back to you. Then, in integrated.py script, you will need to define
{X1, Y1, X2, Y2, X3, Y3, path, and pages} variables (you can find the purpose of variables in comments). If you haves low
internet speed, you can add a delay time for mouse movements or increase the input of time.sleep() function.
Finally, open the destination folder and run the following script in bash to convert images to pdf:
```bash
$ im2pdf.py -i test*.jpg -o test.pdf
```
### Requirements:
```bash
$ pip install -r requirement.txt
```
### License

**Free Software, Hell Yeah!**
