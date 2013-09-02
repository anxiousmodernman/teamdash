teamdash
========

A platform for developing, scheduling, and viewing reports


Technologies
------------
* Django
* AngularJS

Making AngularJS and Django play nicely together requires redefining Angular's template tag. We will follow the tutorial in this video:
http://www.youtube.com/watch?v=Q8FRBGTJ020

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
