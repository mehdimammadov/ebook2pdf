# Online Book to pdf 
### Reason
There are such websites, which allow us to read books, but not to download them. When I don't have
an internet connection, all these books are unvailable. That's why I decided to make this script.

![alt text](https://lh3.googleusercontent.com/proxy/hoDhkyw5FlP7K5Z9gu-w-yzWJ5yr-6-IRgYvJUZfz0hFzRS3PaqRy7USCiosuO1P6dzFjIupLH_WK1JBpitZTtTd3qSxZ7kODIGtkVKiTy23b5HFSI9GTpnYnYiH9ig8vVumVil-YLq0r9qwHbtbVQ)

### About Script
The script was made for copying online books and converting them into pdf format.
The user just needs to give coordinates of the screenshot region and the "next page" button.

### Usage
The script mouse.py returns to you the coordinates of your mouse. Then in integrated.py script,
you need to define  {X1, Y1, X2, Y2, X3, Y3, path, and pages} variables (in comments you can
find the purpose of variables). Also, you can add a delay time for mouse movement or increase
the input of time.sleep() function if you have slow internet.
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
 
