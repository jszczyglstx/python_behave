# python_behave

Run command: For all tests:

behave -D driver=chrome -D base_url=http://the-internet.herokuapp.com/

For single feature file:

behave features/application_form.feature -D driver=chrome -D base_url=http://the-internet.herokuapp.com/

For single tag add:

--tags=@tag_name

For multiple tags add:

--tags=@tag_name1, @tag_name2

Exclude tag/s:

--tags ~@tag_name
