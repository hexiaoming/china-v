var require = {
    baseUrl: "/static",
    paths: {
        'underscore': 'components/underscore/underscore.js',
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
        'backbone': 'components/backbone',

        'ajax_upload': 'ajax_upload/js/ajax-upload-widget',
        'login': 'js/login',
        'students': 'js/backend/students',
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
        },
        'ajax_upload': {
            deps: ['jquery', 'jquery.iframe-transport']
        }
    }
};
