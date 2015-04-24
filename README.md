Inverted Index
Given a directory with books in txt format, write a mapreduce which outputs an inverted index, i.e., a table that associates a word with the books and the corresponding positions at which it occurs (http://en.wikipedia.org/wiki/Inverted_index).

Dataset URL: here
HDFS Cluster DataSet path: /user/hadoop/mapreduce/data/books

hint 1: Suggested output example (not real data): 
Love     alice_in_wonderland.txt:100,the_prince.txt:900,the_prince.txt:1050

hint 2: Given the mapper doesn’t receive the filename as input. A Hadoop Configured Parameter (environment variable) could help to retrieve the filename from which the word comes.


To run this in a hadoop environment, first set up the alias in the .bashrc
```shell
run_mapreduce() {
        hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-x.x.x.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}

```

Because ~ / .bashrc will only run automatically only to start a new instance of the shell is necessary to evaluate the content of the file manually to make the changes effective as of this moment:

```shell
$ source ~/.bashrc

alias hs=run_mapreduce
```

Once the alias has been setup you can either run the process as a MapReduce using the aliased command hs.

eg.

```shell
hs mapper.py reducer.py forum_data inverted_index
```


where:
* "forum_data" is the folder in the HDFS containing the forum node text records
* "inverted_index" is the output data folder, it is important that this folder doesn't already exist.
