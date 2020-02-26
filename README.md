# CSS-Cipher

This is a PoC that generates a pure-CSS substitution cipher that can be used to bypass spam filters for red team/penetration testing engagements. Scanners will see random ASCII characters but the CSS will render in the email client as a string that would otherwise trigger an alert or get quarantined, like "Click here to reset your password."


### Usage

```console
python generate.py "This is what I want to encode"
```

This will generate an `output.html` that contains the CSS and HTML that you can copy into the phishing email that you are crafting.


### Compatibility

This implementation relies on CSS pseudo-elements, which are not supported across all email clients. This hasn't been tested very broadly, but based on my research it should work with the following email clients:

|Support | Client|
|:-:|:-|
|❌|Outlook Desktop|
|✔️|Outlook Mac|
|✔️|Thunderbird|
|✔️|Samsung Native Mail app|
|❌|Gmail App iOS/Android|
|✔️|Applemail|
|✔️|iOS Mail|
|❌|AOL|
|❌|Gmail|
|❌|Outlook.com/Office 365|
|❌|Yahoo!|
