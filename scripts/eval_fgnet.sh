CUDA_VISIBLE_DEVICES=0 python test_fgnet.py --fgnet --verbose --dataroot ../FGNET_with_nvidia_alignment/males --name texture_only256p_ffhq_6classes_lr0001_modulated_conv_pixel_norm_normalize_mlp_decoder_pixel_norm_id10_cyc10_funit_discriminator --which_epoch 400 --gan_mode texture_only --netG stylegan_dec_adain_gen --adain_gen_style_dim 50 --n_downsample_global_tex 2 --ngf 64 --norm pixel --conv_weight_norm --decoder_norm pixel --activation lrelu --use_tanh --use_parsings --use_flow_classes --no_rec_tex --how_many 100 --use_flow_classes --sort_order 0-2,3-6,7-9,15-19,30-39,50-69 --no_facial_hair --no_clothing_items --no_background --adain_one_hot_class_code --upsample_norm adain --normalize_mlp --use_modulated_conv --display_id 0