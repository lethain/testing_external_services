# Testing External Services

[test_ext_blog]: http://lethain.com/ "Testing Django Applications with External Services"

This source code goes along with the blog post [Testing Django Applications With External Services].


## Installation

To pull down the code and experiment:

    git clone ???
    cd testing_external_services
    virtualenv tes
    . ./tes/bin/activate
    pip install -r requirements.txt
    django-admin.py startproject test_project
    python setup.py develop

At that point you're installed and good to go.


## Usage

To run the tests, run:

    ./tes/bin/python/test_project/manage.py test testing_external_services --settings=testing_external_services.test_settings

To run the development server:

    ./tes/bin/python/test_project/manage.py runserver --settings=testing_external_services.test_settings

To run the django shell:

    ./tes/bin/python/test_project/manage.py shell --settings=testing_external_services.test_settings    

