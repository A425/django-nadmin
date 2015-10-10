
vendors = {
    "bootstrap": {
        'js': {
            'dev': 'nadmin/vendor/bootstrap/js/bootstrap.js',
            'production': 'nadmin/vendor/bootstrap/js/bootstrap.min.js',
            'cdn': 'http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js'
        },
        'css': {
            'dev': 'nadmin/vendor/bootstrap/css/bootstrap.css',
            'production': 'nadmin/vendor/bootstrap/css/bootstrap.css',
            'cdn': 'http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css'
        },
        'responsive': {'css':{
                'dev': 'nadmin/vendor/bootstrap/bootstrap-responsive.css',
                'production': 'nadmin/vendor/bootstrap/bootstrap-responsive.css'
            }}
    },
    'jquery': {
        "js": {
            'dev': 'nadmin/vendor/jquery/jquery.js',
            'production': 'nadmin/vendor/jquery/jquery.min.js',
        }
    },
    'jquery-ui-effect': {
        "js": {
            'dev': 'nadmin/vendor/jquery-ui/jquery.ui.effect.js',
            'production': 'nadmin/vendor/jquery-ui/jquery.ui.effect.min.js'
        }
    },
    'jquery-ui-sortable': {
        "js": {
            'dev': ['nadmin/vendor/jquery-ui/jquery.ui.core.js', 'nadmin/vendor/jquery-ui/jquery.ui.widget.js',
                    'nadmin/vendor/jquery-ui/jquery.ui.mouse.js', 'nadmin/vendor/jquery-ui/jquery.ui.sortable.js'],
            'production': ['nadmin/vendor/jquery-ui/jquery.ui.core.min.js', 'nadmin/vendor/jquery-ui/jquery.ui.widget.min.js',
                           'nadmin/vendor/jquery-ui/jquery.ui.mouse.min.js', 'nadmin/vendor/jquery-ui/jquery.ui.sortable.min.js']
        }
    },
    "font-awesome": {
        "css": {
            'dev': 'nadmin/vendor/font-awesome/css/font-awesome.css',
            'production': 'nadmin/vendor/font-awesome/css/font-awesome.min.css',
        }
    },
    "timepicker": {
        "css": {
            'dev': 'nadmin/vendor/bootstrap-timepicker/css/bootstrap-timepicker.css',
            'production': 'nadmin/vendor/bootstrap-timepicker/css/bootstrap-timepicker.min.css',
        },
        "js": {
            'dev': 'nadmin/vendor/bootstrap-timepicker/js/bootstrap-timepicker.js',
            'production': 'nadmin/vendor/bootstrap-timepicker/js/bootstrap-timepicker.min.js',
        }
    },
    "datepicker": {
        "css": {
            'dev': 'nadmin/vendor/bootstrap-datepicker/css/datepicker.css'
        },
        "js": {
            'dev': 'nadmin/vendor/bootstrap-datepicker/js/bootstrap-datepicker.js',
        }
    },
    "flot": {
        "js": {
            'dev': ['nadmin/vendor/flot/jquery.flot.js', 'nadmin/vendor/flot/jquery.flot.pie.js', 'nadmin/vendor/flot/jquery.flot.time.js',
                    'nadmin/vendor/flot/jquery.flot.resize.js','nadmin/vendor/flot/jquery.flot.aggregate.js','nadmin/vendor/flot/jquery.flot.categories.js']
        }
    },
    "image-gallery": {
        "css": {
            'dev': 'nadmin/vendor/bootstrap-image-gallery/css/bootstrap-image-gallery.css',
            'production': 'nadmin/vendor/bootstrap-image-gallery/css/bootstrap-image-gallery.css',
        },
        "js": {
            'dev': ['nadmin/vendor/load-image/load-image.js', 'nadmin/vendor/bootstrap-image-gallery/js/bootstrap-image-gallery.js'],
            'production': ['nadmin/vendor/load-image/load-image.min.js', 'nadmin/vendor/bootstrap-image-gallery/js/bootstrap-image-gallery.js']
        }
    },
    "select": {
        "css": {
            'dev': ['nadmin/vendor/select2/select2.css', 'nadmin/vendor/selectize/selectize.css', 'nadmin/vendor/selectize/selectize.bootstrap3.css'],
        },
        "js": {
            'dev': ['nadmin/vendor/selectize/selectize.js', 'nadmin/vendor/select2/select2.js', 'nadmin/vendor/select2/select2_locale_%(lang)s.js'],
            'production': ['nadmin/vendor/selectize/selectize.min.js', 'nadmin/vendor/select2/select2.min.js', 'nadmin/vendor/select2/select2_locale_%(lang)s.js']
        }
    },
    "multiselect": {
        "css": {
            'dev': 'nadmin/vendor/bootstrap-multiselect/css/bootstrap-multiselect.css',
        },
        "js": {
            'dev': 'nadmin/vendor/bootstrap-multiselect/js/bootstrap-multiselect.js',
        }
    },
    "snapjs": {
        "css": {
            'dev': 'nadmin/vendor/snapjs/snap.css',
        },
        "js": {
            'dev': 'nadmin/vendor/snapjs/snap.js',
        }
    },
}
