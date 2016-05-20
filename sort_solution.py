#! /usr/bin/env python
# -*-coding: utf8 -*-
import random
import time


class sort_solution(object):
    def swap(self,list1,i,j):
        tmp = list1[i]
        list1[i] = list1[j]
        list1[j] = tmp
    
    
    
    def choose_sort(self,list2Sort):
        '''
        doc
        '''
        list_length = len(list2Sort)
        for i in range(0,list_length-1):
            min_index = i
            for j in range(i+1,list_length):
                if list2Sort[j] < list2Sort[min_index]:
                    min_index = j
            if i != min_index:
                self.swap(list2Sort, i,min_index)
        return list2Sort
    
    def bubble_sort(self,list2Sort):
        list_length = len(list2Sort)
        for i in range(0,list_length -1):
            for j in range(0,list_length-1-i):
                if list2Sort[j] > list2Sort[j+1]:
                    self.swap(list2Sort, j ,j+1)
        return list2Sort
    
    def insert_sort(self,list2Sort):
        list_length = len(list2Sort)
        for i in range(0 ,list_length-1):
            current = list2Sort[i+1]
            j = i+1
            while (j > 0 and current < list2Sort[j-1]):
                list2Sort[j] = list2Sort[j-1]
                j = j-1
            list2Sort[j] = current
        return list2Sort 
    
    def check_right(self,sort_func):
        list_test = [22, 21, 20, 29, 35, 35, 63, 12, 6, 68, 8, 41, 73, 50, 14, 19, 50, 75, 62, 41]
        list_sorted = [6, 8, 12, 14, 19, 20, 21, 22, 29, 35, 35, 41, 41, 50, 50, 62, 63, 68, 73, 75]
        if sort_func(list_test) == list_sorted:
            print "func %s is right"%sort_func
            #print help(sort_func)
        else:
            print "func %s is wrong!!!!  the result is :"%sort_func
            print list_test
            print list_sorted
    
    def check_performance(self,sort_func):
        list1 = []
        for i in range(20000):
            list1.append(random.randint(0,10000))
        time_start = time.time()
        sort_func(list1)
        time_end = time.time()
        print "%s takes %f second"%(sort_func,time_end - time_start)

    def quick_sort(self,list2Sort):
        list_length = len(list2Sort)
        def quick_sort_core(list2Sort,first,last):
            if first < last:
                mid = partition(list2Sort, first, last)
                #print list2Sort,first,mid,last,list2Sort[mid]
                quick_sort_core(list2Sort, first, mid - 1)
                quick_sort_core(list2Sort, mid+1 , last)
        def partition(list2Sort, first, last):
            part_ele = list2Sort[first]
            while first < last:
                while first < last and list2Sort[last] >= part_ele:    #  TAKE CARE OF THE = !!!
                    last = last - 1
                list2Sort[first] = list2Sort[last]
                while first < last and list2Sort[first] <= part_ele:
                    first = first + 1
                list2Sort[last] = list2Sort[first]
            list2Sort[first] = part_ele
            return first
        quick_sort_core(list2Sort,0,list_length -1)
        return list2Sort

    def merge_sort(self, list2Sort):
        list_length = len(list2Sort)
        list_tmp = [ 0 for i in range(list_length) ]
        def merge_sort_core(list2Sort, first, last, list_tmp):
            if first <last :
                mid = (first + last)/2
                merge_sort_core(list2Sort,first, mid, list_tmp)
                merge_sort_core(list2Sort,mid+1 , last ,list_tmp)
                merge_array(list2Sort,first, mid , last, list_tmp)
        def merge_array(list2Sort, first, mid ,last ,list_tmp):
            i = first
            j = mid + 1
            k = 0
            while i <= mid and j <= last:
                if list2Sort[i] < list2Sort[j]:
                    list_tmp[k] = list2Sort[i]
                    k += 1
                    i += 1
                else:
                    list_tmp[k] = list2Sort[j]
                    k += 1
                    j += 1
            while i <= mid :
                list_tmp[k] = list2Sort[i]
                k += 1
                i += 1
            while j <= last:
                #print k,j,list2Sort
                list_tmp[k] = list2Sort[j]
                k += 1
                j += 1
            for i in range(k):   #COPY THE TEMP TO THE REAL ARRAY
                list2Sort[first + i] = list_tmp[i]
        merge_sort_core(list2Sort,0 , list_length - 1, list_tmp)
        return list2Sort
    def heap_sort(self,list2Sort):
        def heap_adjust(list2Sort,ele_index,list_length):
            lchild = 2 * ele_index +1
            rchild = lchild + 1
            max_child = lchild
            while(lchild < list_length):    #take care of the boundry condition
                if rchild < list_length and list2Sort[rchild] > list2Sort[lchild]:
                    max_child = rchild
                if max_child < list_length and list2Sort[max_child]> list2Sort[ele_index]:
                    self.swap(list2Sort, max_child, ele_index)
                ele_index = max_child
                lchild = 2* ele_index + 1
                rchild = lchild + 1
                max_child = lchild
        list_length = len(list2Sort)
        for i in range((list_length-1)/2,-1,-1):
            heap_adjust(list2Sort,i,list_length)
        for i in range(list_length-1, 0 , -1):
            self.swap(list2Sort,0,i)
            heap_adjust(list2Sort,0,i)
        return list2Sort



if __name__ == "__main__":
    solu1 = sort_solution()
    solu1.check_right(solu1.heap_sort)
    #solu1.check_performance(solu1.insert_sort)
    #solu1.check_performance(solu1.bubble_sort)
    #solu1.check_performance(solu1.choose_sort)
    #solu1.check_performance(solu1.quick_sort)
    #solu1.check_performance(solu1.merge_sort)
    #solu1.check_performance(solu1.heap_sort)
    #check_performance(choose_sort)
    #check_performance(bubble_sort)
    #check_performance(insert_sort)
