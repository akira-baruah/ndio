import unittest
import ndio.remote.OCP as OCP
import ndio.ramon
import ndio.utils.autoingest as AutoIngest
import numpy

SERVER_SITE = 'http://http://ec2-54-200-94-232.us-west-2.compute.amazonaws.com/'
DATA_SITE = 'http://ec2-54-200-215-161.us-west-2.compute.amazonaws.com/'

class TestAutoIngest(unittest.TestCase):

    def setUp(self):
        self.oo = OCP(SERVER_SITE)
        self.i = datetime.datetime.now()


    def test_pull_data(self):
        data_name_1 = "ndio_test_1_%s:%s:%s:%s:%s:%s" % (self.i.day, self.i.month, self.i.year, self.i.hour, self.i.month, self.i.second)

        ai_1 = AutoIngest.AutoIngest()
        ai_1.add_channel(data_name_1, 'uint32', 'image',
                    DATA_SITE, 'SLICE', 'tif')

        ai_1.add_project(data_name_1, data_name_1, 1)
        ai_1.add_dataset(data_name_1, (660, 528, 1), (0, 0, 0))
        ai_1.add_metadata('')

        ai_1.post_data(SERVER_SITE)
        numpy_download = self.oo.get_cutout(data_name_1, data_name_1,
                                            0, 660,
                                            0, 528,
                                            0, 0,
                                            resolution=0)

        self.assertEqual(type(numpy_download), numpy.ndarray)
        #Verify its the same image?
        self.oo.delete_channel(data_name_1, data_name_1)


    def test_post_json(self):
        data_name_2 = "ndio_test_2_%s:%s:%s:%s:%s:%s" % (self.i.day, self.i.month, self.i.year, self.i.hour, self.i.month, self.i.second)

        ai_2 = AutoIngest.AutoIngest()
        ai_2.add_channel(data_name_2, 'uint32', 'image',
                    DATA_SITE, 'SLICE', 'tif')

        ai_2.add_project(data_name_2, data_name_2, 1)
        ai_2.add_dataset(data_name_2, (660, 528, 1), (0, 0, 0))
        ai_2.add_metadata('')

        ai_2.output_json()

        ai_3 = AutoIngest.AutoIngest()
        ai_3.post_data(SERVER_SITE, "/tmp/ND.json")

        numpy_download = self.oo.get_cutout(data_name_2, data_name_2,
                                            0, 660,
                                            0, 528,
                                            0, 0,
                                            resolution=0)

        self.assertEqual(type(numpy_download), numpy.ndarray)

        self.oo.delete_channel(data_name_2, data_name_2)

if __name__ == '__main__':
    unittest.main()