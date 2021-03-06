import unittest
import ndio.remote.OCP as OCP
import ndio.ramon
import ndio.convert.png as ndpng
import ndio.convert.tiff as ndtiff
import numpy


class TestDownload(unittest.TestCase):

    def setUp(self):
        self.oo = OCP()

    def test_export_import_png(self):
        # kasthuri11/image/xy/3/1000,1100/1000,1100/1000/
        image_download = self.oo.get_image('kasthuri11', 'image',
                                           1000, 1100,
                                           1000, 1100,
                                           1000,
                                           resolution=3)

        # if returns string, successful export
        self.assertEqual(
                ndpng.export_png("tests/trash/download.png", image_download),
                "tests/trash/download.png")

        # now confirm import works too
        self.assertEqual(ndpng.import_png("tests/trash/download.png")[0][0],
                         image_download[0][0])
        self.assertEqual(ndpng.import_png("tests/trash/download.png")[10][10],
                         image_download[10][10])

    def test_export_import_tiff(self):
        # kasthuri11/image/xy/3/1000,1100/1000,1100/1000/
        image_download = self.oo.get_image('kasthuri11', 'image',
                                           1000, 1100,
                                           1000, 1100,
                                           1000,
                                           resolution=3)

        # if returns string, successful export
        self.assertEqual(
                ndtiff.export_tiff("tests/trash/download-1.tiff", image_download),
                "tests/trash/download-1.tiff")

        # now confirm import works too
        self.assertEqual(ndtiff.import_tiff("tests/trash/download-1.tiff")[0][0],
                         image_download[0][0])
        self.assertEqual(ndtiff.import_tiff("tests/trash/download-1.tiff")[10][10],
                         image_download[10][10])


if __name__ == '__main__':
    unittest.main()
