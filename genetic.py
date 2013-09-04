#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Artem'
import random
#решение диофантового уравнения
#вида a+b+c+d+e=x

#корни лежат на отрезке от 1 до x
#функция возвращает случайные значения от 1 до x
def population(rang,summands):
    a=[]
    for i in range(1,summands):
        a.append(random.randint(0,rang))
    return a
#создаем хромосомы
def initialPopulations(equations,rang,summands):
    a=[]
    for i in range(1,equations):
        a.append(population(rang,summands))
    return a
#вычисляем целевую функцию для каждой хромосомы
#a-массив хромосом, k-массив коэффициентов
def fitFunction(a,k,value):
    fit=[]
    for populat in a:
        sum=0
        for i in range(len(populat)):
            sum+=populat[i]*k[i]
        if (abs(sum-value)==0):
            return (True,populat)
        fit.append(abs(sum-value))
    return fit
#считаем вероятность выбора каждой хромосомы
def countProbability(fit):
    sum=0
    p=[]
    for item in fit:
        sum+=1./item
    for item in fit:
        p.append(1./item/sum)
    return p
def getIndex(val,probability):
    last=0
    for i in range(len(probability)):
        if (last <= val and val <= probability[i]):
            return i
    else:
        last = probability[i];
    return len(probability)-1
def calculateParents(n,probability):
    parents=[]
    for i in range(1,n):
        val=random.randint(1,100)
        parent1=getIndex(val,probability)
        val=random.randint(1,100)
        parent2=getIndex(val,probability)
        while (parent1==parent2):
            val=random.randint(1,100)
            parent2=getIndex(val,probability)
        tuple=(parent1,parent2)
        parents.append(tuple)
    return parents
def breed(parents,length,chrom):
    new_chrom=[]
    for tuple in parents:
        crossover=random.randint(0,length-1)
        buffer=[]
        for i in range(0,crossover):
            buffer.append(chrom[tuple[0]][i])
        for i in range(crossover+1,len(chrom[tuple[1]])):
            buffer.append(chrom[tuple[1]][i])
        new_chrom.append(buffer)
    return new_chrom

#решим уравнение вида a+2b+3c+4d=30
pop=initialPopulations(10,30,4)
coefficients=[1,2,3,4]
fit=fitFunction(pop,coefficients,30)
while (fit[0]!=True):
    probability=countProbability(fit)
    parents=calculateParents(10,probability)
    pop=breed(parents,4,pop)
    fit=fitFunction(pop,coefficients,30)
print "Решение уравнения: "+fit[1]

