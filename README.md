# Gif image uploader

## Python script that uploads a gif to either Imgur or Giphy using the [Imgur api](https://apidocs.imgur.com/) and [Giphy api](https://developers.giphy.com/docs/api) copies the link to your clipboard.

<br/>

### This is a quicker, less UI oriented approach to uploading gifs. It removes the need of opening a browser, navigating to [Imgur](https://imgur.com/) or [Giphy](https://giphy.com/), finding the gif in your file system, uploading it and copying the link to your clipboard.

<br/>

**_Note:_** There are some upload restrictions applied when using the free versions of these APIs. Imgur has a **file size limit** for gifs uploaded via their API, and Giphy allows only **10 free** uploads per day. Because of this, the script will initially attempt an upload to Imgur, and upon failure due to file size, will upload to Giphy.

Also included in this repo is a template bash script (script.sh) that sources the python virtual env, runs the script and deactivates the env. I personally have this script in my default usr directory so I can quickly open a terminal and execute it.
<br/>
<br/>

### Here is some gif-ception (I uploaded a gif of me using this tool to upload a gif):

<br/>

![](https://i.imgur.com/gIaz1OO.gif)
