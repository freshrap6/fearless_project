So this is my 5 take on the project. There are so many different ways to do it.

Getting items
 - GET /items

Delete items
 - DELETE /items

Edit items
 - PUT /items/id

Dockerfile
Config file to host port

My plan of attack. Create minimial app. get it working with dockerfile and config. Implement the API. Add database. Do testing along the way.

/api will be the root of the request

each resource will have its own folder and source file


TODOS:
More Unit testing
Type hinting
Improved Configuration
Adding more resources for item
 - per id 


Known Issues:
Put must be in the form of {data:[{"name":"value"}]}
Can only handle a single update
Repea