var require = {
    baseUrl: "/static",
    paths: {
        'jquery': 'components/jquery/dist/jquery.min',
        'jquery.iframe-transport': 'components/jquery.iframe-transport/jquery.iframe-transport',
        'select2': 'components/select2/select2',
        'bootstrap': 'components/bootstrap/dist/js/bootstrap.min',
        'jquery-placeholder': 'components/jquery-placeholder/jquery.placeholder',
        'jquery.cookie': 'components/jquery.cookie/jquery.cookie',
        'jquery.serializeObject': 'components/jQuery.serializeObject/dist/jquery.serializeObject.min',
        'django-csrf-support': 'components/django-csrf-support/index',
        'underscore': 'components/underscore/underscore',
        'multiline': 'components/multiline/browser',
        'login': 'js/login',
        'promotion': 'js/promotion/promotion',
        'swiper': 'components/swiper/dist/idangerous.swiper.min'
    },
    shim: {
        'jquery-placeholder': {
            deps: ['jquery']
        },

        'jquery.serializeObject': {
            deps: ['jquery']
        },
        'select2': {
            deps: ['jquery']
        },
        'bootstrap': {
            deps: ['jquery']
        },
        'jquery.cookie': {
            deps: ['jquery']
        }
    }
};
