#!/bin/python

#list inside dict
studentDict = dict(
  student1=['joe','smith'],
  student2=['mary','jones'],
  student3=['sally','brown']
)

#dict inside dict
studentDict2 = dict(
  student1=dict(first='joe',last='smith'),
  student2=dict(first='mary',last='jones'),
  student3=dict(first='sally',last='brown')
)

#List inside list

studentList = [ 
  ['joe', 'smith'], 
  ['mary', 'jones'], 
  ['sally', 'brown'] 
]

#Dict inside List

studentList2 = [ 
  dict(first='joe',last='smith'), 
  dict(first='mary',last='jones'),
  dict(first='sally',last='brown')
]
