# Ajax from scratch

<a href="http://julien.muetton.me/" class="author">Julien Muetton</a>
<p class="conference"><span class="name">API Hours</span> <span class="location">CFE</span></p>
<p class="date">2013 April, 3rd</p>

.fx: main-title

---

## Summary

* What is AJAX
* XMLHttpRequest
* Promise API

.fx: summary

---

## History

* **1998**: XMLHttpRequest ActiveX introduced by Microsoft
* **2002**: Introduced in ECMAScript specifications
* **2002-2005**: implemented in major browsers
* **2005**: AJAX first introduced by `Jesse James Garrett`

.fx: xhr-history

---

## What is AJAX?

> **A**synchronous **J**ava**S**cript and **X**ML

### ECMAScript HTTP API

Request data from server without page reload

### Javascript to request data

`XMLHttpRequest` object.

### Normalize communications

`XML` or `JSON` formatted.

---

## Typical call

<div class="diagram" style=""> Browser->Server: Asks a page
Note Right of Server: Compute the page
Server->Browser: Returns HTML
Note Left of Browser: User interacts\nwith the page
Browser-->Server: Asks for data
Note Right of Server: Looks for data
Server-->Browser: returns data in JSON, XML...
Note Left of Browser: Data are processed\nthrough callback</div>

---

# XMLHttpRequest

---

## XMLHttpRequest

### Can be Synchronous or asynchronous

Yes Indeed...

### Single object for Request and Response

* Methods;
* Public properties;
* Event handlers.

### Implementation evolved over the years.

* Use new stuff if you know your customers;
* Use a library to deal with a single API.

---

## Cross browser creation

    !js
    function createXhrObject() {
        if (window.XMLHttpRequest)
            return new XMLHttpRequest();

        if (window.ActiveXObject) {
            var names = [
                "Msxml2.XMLHTTP.6.0", "Msxml2.XMLHTTP.3.0",
                "Msxml2.XMLHTTP", "Microsoft.XMLHTTP"
            ];
            for(var i in names) {
                try{ return new ActiveXObject(names[i]); }
                catch(e){}
            }
        }
        window.alert("XMLHTTPRequest isn't supported.");
        return null;
    }
    xhr = createXhrObject();

---

## XMLHttpRequest: Request

### Prepare

* `void open(method, url, async = true, user = null, password = null);`
* `void setRequestHeader(ByteString header, ByteString value);`

### Send

* `void send(data = null);`

### Abort

* `void abort();`

---

## XMLHttpRequest: Response

### Read status

* `status`: response HTTP status
* `statusText`: Human readable HTTP status

### Access server response

* [`response`](http://www.w3.org/TR/XMLHttpRequest/#dom-xmlhttprequest-response): depends of content type
* `responseText`: raw response
* `responseXML`: Only for XML responses

### Response headers

* `string getResponseHeader(headerName);`
* `string getAllResponseHeaders();`

---

## Event driven: Old way

> A single event: `onreadystatechange`

* `xhr.UNSENT = 0`
* `xhr.OPENED = 1`
* `xhr.HEADERS_RECEIVED = 2`
* `xhr.LOADING = 3`
* `xhr.DONE = 4`

---

## Sample usage

    !js
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        switch (this.readyState) {
            case this.LOADING:
                // Use this for long polling
                break;

            case this.DONE:
                if (/^2/.test(this.status)) {
                    // success
                } else {
                    // failure
                }
        }
    }

    xhr.open('GET', 'http://example.org/ressources/1');
    xhr.send();

---

## Event driven: New way

introduced in `XMLHttpRequest Level 2`, 25 February 2008

> Attach event listeners through
>   `addEventListener(name, callback);`

* `loadstart`: When the request starts.
* `progress`: While sending and loading data.
* `abort`: When the request has been aborted. For instance, by invoking the abort() method.
* `error`: When the request has failed, **based on network, not status code**.
* `load`: When the request has successfully completed.
* `timeout`: When the author specified timeout has passed before the request could complete.
* `loadend`: When the request has completed (either in success or failure).

---

## Sample usage

    !js
    var xhr = new XMLHttpRequest();
    xhr.addEventListener('load', function () {
        if (/^2/.test(xhr.status)) {
            // success
        } else {
            // failure
        }
    }
    xhr.addEventListener('error', function () {
        // something went wrong
    }
    xhr.addEventListener('progress', function () {
        // Use for long polling
    }

    xhr.open('GET', 'http://example.org/ressources/1');
    xhr.send();

---

# Promise API: leverage asynchronous

---

## Promise?

* [Promises](http://wiki.commonjs.org/wiki/Promises) are CommonJS spec (/A, /B, /C, /D) ;
* Functional approach for asynchronous ;
* A single API for every asynchronous processes ;
* Avoid pyramid of doom.

.fx: promises

---

## Quick jQuery example

.warning: jQuery is none of CommonJS Promize compliant but is consistent.

    !js
    $.ajax( "/example" )

        // when request is successful
        .done(function(response) { alert("success"); })

        // Error happened
        .fail(function(xhr, statusText, error) {
            alert("error"); })

        // executed in both cases
        .always(function() { alert("complete"); });

---

## Combine

.info: Note there is a single callback to handle all returned data.

    !js
    $.when(
        $.ajax("/example"),
        $.ajax("/sample")
    )

    // called when both succeed
    .done(function (example, sample) {
        alert ('both returned');
    })

    // called when any request fails
    .fail(function () { /* ... */ });

---

## Pipe

    !js
    $.ajax( "/example" )
        .fail(function () {
            alert('example failed')
        })
        .pipe(
            function success(example) {
                return $.ajax('/sample');
            },
            function error() {
                alert('example failed !')
            })

        // From here, this is about second request
        .done(function (sample) {
            alert ('sample returned');
        })
        .fail(function () {
            alert('sample failed')
        });

---

## Filter data

.info: Easy way to tweak inconsistant apis.

    !js
    $.ajax( "/example" )
        .then(
            function success(example) {
                // filter data
                return {response: example};
            },
            function error() { /*...*/ },
            function progress() { /*...*/ }
        )

        // `data` has been altered by `then` callback
        .done(function (data) {
            console.log(data.response);
        });

---

## What's next?

* use [`$.Deferred`](http://api.jquery.com/category/deferred-object/) for all async processes ;
* [<accronym title="Cross Origin Ressource Sharing">CORS</accronym>](Cross Origin Ressource Sharing) for cross domain requests ;
* [`WebSockets`](http://www.w3.org/TR/websockets/): HTTP PubSub ;
* [async](https://github.com/caolan/async) utilities for node and the browser.

.fx: what-s-next

---

# Questions?

---

# Thank you
