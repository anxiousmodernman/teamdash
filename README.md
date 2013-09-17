teamdash
========

A platform for developing, scheduling, and viewing reports


Setup 
----------------------------
1. Create a Python virtualenv
2. install the requirements.txt
3. Configure your IDE


Technologies
------------
* Django
* AngularJS
* Django REST Framework
* Celery


AngularJS Templates
-------------------
Making AngularJS and Django play nicely together requires redefining Angular's template tag. We will follow the tutorial in this video:
http://www.youtube.com/watch?v=Q8FRBGTJ020
...which features code from [this repository|https://github.com/gkappel/demo-d201305/blob/master/demo/static/js/demo.js]

```javascript
/* AngularJS app definition */
var shopping = angular.module('shopping',['ngCookies']);

shopping.config(function($interpolateProvider) {
    //allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// define controllers, factories, etc below...
```


Celery: our message queue
-------------------------
An informative blog post on using Celery with async JavaScript is here: https://zapier.com/blog/async-celery-example-why-and-how/
