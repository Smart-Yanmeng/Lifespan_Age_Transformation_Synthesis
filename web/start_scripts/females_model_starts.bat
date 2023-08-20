echo starting...

cd ..

set CUDA_VISIBLE_DEVICES=0

python test.py --name females_model --which_epoch latest --display_id 0 --traverse --interp_step 0.05 --image_path_file male_image_list.txt --make_video --in_the_wild --verbose
