import sys
sys.path.append('./modules/')

from knn import execute as execute_knn
from kmeans import execute as execute_k_means




execute_k_means("iris_teste.txt",5,0)