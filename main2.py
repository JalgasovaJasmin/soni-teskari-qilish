#17. Har xil hajmdagi nuqtalar bilan nuqta grafik (bubble plot) chizing.
#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

#df = pd.DataFrame({
#      'x': np.random.rand(40),
#      'y': np.random.rand(40),
#      'z': np.random.rand(40),
#   })
#df.head()
#plt.scatter(df['x'], df['y'], s=df['z']*1000, alpha=0.5,c="red")


#plt.xlabel("X o'qi")
#plt.ylabel("Y o'qi")
#plt.title("A bubble plot", loc="left")
#plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()
