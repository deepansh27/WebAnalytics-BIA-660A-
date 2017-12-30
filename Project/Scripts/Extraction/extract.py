from ExtractReviews import ExtractReviews

base_input_path = '/Users/deepanshparab/Desktop/Projects/Bia-660/Project/ScrappedData/Indian'
base_output_path = '/Users/deepanshparab/Desktop/Projects/Bia-660/Project/ExtractedReviews'
extract = ExtractReviews(base_input_path,base_output_path)

extract.extractRestaurant(base_input_path, base_output_path)
