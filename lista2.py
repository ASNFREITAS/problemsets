#!/usr/bin/env python3

taxa = ("sapiens, erectus, neanderthalensis")

print(taxa)

print(taxa[1])
print(type(taxa))
species = taxa.split(",")
print(species)
print(species[1])
print(type(species))
species.sort()
print (species)
def myFunc(e):
  return len(e)
species.sort(key=myFunc)
print(species)
