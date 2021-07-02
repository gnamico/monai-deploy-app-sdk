import sys
sys.path.insert(0,'../../../../')

from monai.deploy.foundation.base_operator import BaseOperator

from skimage import data
from skimage.morphology import disk
from skimage.filters import median
from skimage.io import imsave

class MedianOperator(BaseOperator):

    """ This Operator implements a noise reduction
    algorithm based on median operator. It
    ingest a single input and provides a single output
    """
    def __init__(self):
        super().__init__()
        self.data_out = None
    

    def get_output(self, index):
        return self.data_out
    

    def execute(self):
        super().execute()
        data_in = self.get_input(0)
        self.data_out = median(data_in)