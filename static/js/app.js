(function() {
  var app = angular.module('myApp', [])

  app.controller('articleListController',['$http', '$log', function($http, $log) {
    var site = this;
    site.articles = [];
    $http.get('/article/list/').success(function(data) {
    	site.articles = data;
    });
  }]);

  app.controller('articleNavigationController', ['$http', '$log', function($http, $log) {
  	var navigation = this;
  	$http.get('/article/navigation/').success(function(data) {
  		navigation.articles = data;
  	});
  }]);

  app.directive('articleList', function() {
	  	return {
	  		restrict: 'E',
	  		templateUrl: '/article/list/html/'
	  	}
  });

  app.directive('navbar', function() {
  		return {
	  		restrict: 'E',
	  		templateUrl: '/navigation/html/'
	  	}
  });

})();
