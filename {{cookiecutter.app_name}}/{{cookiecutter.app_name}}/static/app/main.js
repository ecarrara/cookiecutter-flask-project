require.config({
    baseUrl: '/static',
    paths: {
        jquery: 'lib/jquery/jquery',
        bootstrap: 'lib/bootstrap/dist/js/bootstrap'
    },
    shim: {
        bootstrap: {
            deps: ['jquery']
        }
    }
});

require([
    'jquery',
    'bootstrap',
], function () {

    console.log('Hello world!');

});
