# CSSipher

This is a PoC that generates a pure-CSS substitution cipher that can be used to bypass spam filters for red team/penetration testing engagements.

### Usage

```console
python generate.py "This is what I want to encode"
```

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