import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

##############################################################################
parameter = 'alpha'
channel = 'green'
call_folder = 'model_green_alpha_classes_5_VGG16_150_no_preprocessing/'
##############################################################################

avg_loss_plot = np.load(call_folder + channel + '_' + parameter + '_avg_loss_plot.npy')
val_accuracy_plot = np.load(call_folder + channel + '_' + parameter + '_val_accuracy_plot.npy')
test_accuracy_plot = np.load(call_folder + channel + '_' + parameter + '_test_accuracy_plot.npy')

plt.figure(1)
plt.plot(range(1, len(avg_loss_plot) + 1), avg_loss_plot)
plt.title('Training loss for ' + channel + '_' + parameter)
plt.xlabel('Epoch')
plt.ylabel('Average Training Loss')
plt.savefig(call_folder + channel + '_' + parameter + '_TrainLoss.jpg')

plt.figure(2)
plt.plot(range(1, len(val_accuracy_plot) + 1), val_accuracy_plot, label='Validation Accuracy')
plt.plot(range(1, len(test_accuracy_plot) + 1), test_accuracy_plot, label='Test Accuracy')
plt.title('Accuracy for ' + channel + '_' + parameter)
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig(call_folder + channel + '_' + parameter + '_Acccuracy.jpg')
