Hacking JQuery Bootgrid
====

There are a number of these JavaScript data grids floating around. At work, we
have been using one that's not the newest revision and which is kind of a pain
in various ways. So this is a quick investigation of JQuery's preferred data
grid, which looks pretty good.

We are particularly interested in doing sorting, searching and pagination on the
server side, and Bootgrid allows that.

Normally the POST parameters for sorting, search and pagination would be mapped
to database operations, since there are pretty obvious SQL analogies for all of
them and databases do those things very efficiently. But I didn't want to bother
with a database in this exercise as it would have vastly complicated things, so
there is Python code that pretends to do those things, using a very small data
set of movies.

Thanks to
[this critique of virtualenv's activate script](https://gist.github.com/datagrok/2199506),
I was able to put all the virtualenv stuff into the `go.sh` script so you don't
need to fool around with `activate` and `deactivate`. Nice.