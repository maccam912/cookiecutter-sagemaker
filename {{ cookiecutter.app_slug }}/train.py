import pickle
from model import Model

m = Model()
print(m.invoke("test"))
pickle.dump(m, open("/opt/ml/model/model.pkl", "wb"))
