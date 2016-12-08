(function() {
  var app = angular.module('myApp', [])

  app.controller('articleListController',['$http', '$log', function($http, $log){
    site = this;
    site.articles = [];
    $http.get('/article/list/').success(function(data){
    	site.articles = data;
    });

  }]);

  app.directive('articleList', function(){
	  	return {
	  		restrict: 'E',
	  		templateUrl: '/article/list/html/'
	  	}
	});

})();
