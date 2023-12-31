auto_scale_lr = dict(base_batch_size=1024)
backend_args = dict(backend='local')
base_lr = 0.004
codec = dict(
    heatmap_size=(
        48,
        64,
    ),
    input_size=(
        192,
        256,
    ),
    sigma=2,
    type='UDPHeatmap')
custom_hooks = [
    dict(
        ema_type='ExpMomentumEMA',
        momentum=0.0002,
        priority=49,
        type='EMAHook',
        update_buffers=True),
    dict(
        switch_epoch=180,
        switch_pipeline=[
            dict(backend_args=dict(backend='local'), type='LoadImage'),
            dict(type='GetBBoxCenterScale'),
            dict(direction='horizontal', type='RandomFlip'),
            dict(type='RandomHalfBody'),
            dict(
                rotate_factor=60,
                scale_factor=[
                    0.75,
                    1.25,
                ],
                shift_factor=0.0,
                type='RandomBBoxTransform'),
            dict(input_size=(
                192,
                256,
            ), type='TopdownAffine', use_udp=True),
            dict(type='mmdet.YOLOXHSVRandomAug'),
            dict(
                transforms=[
                    dict(p=0.1, type='Blur'),
                    dict(p=0.1, type='MedianBlur'),
                    dict(
                        max_height=0.4,
                        max_holes=1,
                        max_width=0.4,
                        min_height=0.2,
                        min_holes=1,
                        min_width=0.2,
                        p=0.5,
                        type='CoarseDropout'),
                ],
                type='Albumentation'),
            dict(
                encoder=dict(
                    heatmap_size=(
                        48,
                        64,
                    ),
                    input_size=(
                        192,
                        256,
                    ),
                    sigma=2,
                    type='UDPHeatmap'),
                type='GenerateTarget'),
            dict(type='PackPoseInputs'),
        ],
        type='mmdet.PipelineSwitchHook'),
]
data_mode = 'topdown'
data_root = '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/'
dataset_aic = dict(
    ann_file='aic/annotations/aic_train.json',
    data_mode='topdown',
    data_prefix=dict(
        img=
        'pose/ai_challenge/ai_challenger_keypoint_train_20170902/keypoint_train_images_20170902/'
    ),
    data_root=
    '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/',
    pipeline=[
        dict(
            mapping=[
                (
                    0,
                    6,
                ),
                (
                    1,
                    8,
                ),
                (
                    2,
                    10,
                ),
                (
                    3,
                    5,
                ),
                (
                    4,
                    7,
                ),
                (
                    5,
                    9,
                ),
                (
                    6,
                    12,
                ),
                (
                    7,
                    14,
                ),
                (
                    8,
                    16,
                ),
                (
                    9,
                    11,
                ),
                (
                    10,
                    13,
                ),
                (
                    11,
                    15,
                ),
                (
                    12,
                    17,
                ),
                (
                    13,
                    18,
                ),
            ],
            num_keypoints=19,
            type='KeypointConverter'),
    ],
    type='AicDataset')
dataset_coco = dict(
    dataset=dict(
        ann_file=
        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/annotations/person_keypoints_train2017.json',
        data_mode='topdown',
        data_prefix=dict(
            img=
            '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/images/train2017/'
        ),
        data_root=
        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/',
        pipeline=[
            dict(
                mapping=[
                    (
                        0,
                        0,
                    ),
                    (
                        1,
                        1,
                    ),
                    (
                        2,
                        2,
                    ),
                    (
                        3,
                        3,
                    ),
                    (
                        4,
                        4,
                    ),
                    (
                        5,
                        5,
                    ),
                    (
                        6,
                        6,
                    ),
                    (
                        7,
                        7,
                    ),
                    (
                        8,
                        8,
                    ),
                    (
                        9,
                        9,
                    ),
                    (
                        10,
                        10,
                    ),
                    (
                        11,
                        11,
                    ),
                    (
                        12,
                        12,
                    ),
                    (
                        13,
                        13,
                    ),
                    (
                        14,
                        14,
                    ),
                    (
                        15,
                        15,
                    ),
                    (
                        16,
                        16,
                    ),
                ],
                num_keypoints=19,
                type='KeypointConverter'),
        ],
        type='CocoDataset'),
    times=3,
    type='RepeatDataset')
dataset_type = 'CocoDataset'
default_hooks = dict(
    badcase=dict(
        badcase_thr=5,
        enable=False,
        metric_type='loss',
        out_dir='badcase',
        type='BadCaseAnalysisHook'),
    checkpoint=dict(
        interval=10,
        max_keep_ckpts=1,
        rule='greater',
        save_best='coco/AP',
        type='CheckpointHook'),
    logger=dict(interval=50, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(enable=False, type='PoseVisualizationHook'))
default_scope = 'mmpose'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
keypoint_mapping_aic = [
    (
        0,
        6,
    ),
    (
        1,
        8,
    ),
    (
        2,
        10,
    ),
    (
        3,
        5,
    ),
    (
        4,
        7,
    ),
    (
        5,
        9,
    ),
    (
        6,
        12,
    ),
    (
        7,
        14,
    ),
    (
        8,
        16,
    ),
    (
        9,
        11,
    ),
    (
        10,
        13,
    ),
    (
        11,
        15,
    ),
    (
        12,
        17,
    ),
    (
        13,
        18,
    ),
]
keypoint_mapping_coco = [
    (
        0,
        0,
    ),
    (
        1,
        1,
    ),
    (
        2,
        2,
    ),
    (
        3,
        3,
    ),
    (
        4,
        4,
    ),
    (
        5,
        5,
    ),
    (
        6,
        6,
    ),
    (
        7,
        7,
    ),
    (
        8,
        8,
    ),
    (
        9,
        9,
    ),
    (
        10,
        10,
    ),
    (
        11,
        11,
    ),
    (
        12,
        12,
    ),
    (
        13,
        13,
    ),
    (
        14,
        14,
    ),
    (
        15,
        15,
    ),
    (
        16,
        16,
    ),
]
launcher = 'pytorch'
load_from = None
log_level = 'INFO'
log_processor = dict(
    by_epoch=True, num_digits=6, type='LogProcessor', window_size=50)
max_epochs = 210
model = dict(
    backbone=dict(
        _scope_='mmdet',
        act_cfg=dict(type='SiLU'),
        arch='P5',
        channel_attention=True,
        deepen_factor=1.0,
        expand_ratio=0.5,
        init_cfg=dict(
            checkpoint=
            'https://download.openmmlab.com/mmdetection/v3.0/rtmdet/cspnext_rsb_pretrain/cspnext-l_8xb256-rsb-a1-600e_in1k-6a760974.pth',
            prefix='backbone.',
            type='Pretrained'),
        norm_cfg=dict(type='SyncBN'),
        out_indices=(4, ),
        type='CSPNeXt',
        widen_factor=1.0),
    data_preprocessor=dict(
        bgr_to_rgb=True,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='PoseDataPreprocessor'),
    head=dict(
        decoder=dict(
            heatmap_size=(
                48,
                64,
            ),
            input_size=(
                192,
                256,
            ),
            sigma=2,
            type='UDPHeatmap'),
        in_channels=1024,
        loss=dict(type='KeypointMSELoss', use_target_weight=True),
        out_channels=19,
        type='HeatmapHead'),
    test_cfg=dict(
        flip_test=False,
        output_keypoint_indices=[
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
        ]),
    type='TopdownPoseEstimator')
optim_wrapper = dict(
    optimizer=dict(lr=0.004, type='AdamW', weight_decay=0.05),
    paramwise_cfg=dict(
        bias_decay_mult=0, bypass_duplicate=True, norm_decay_mult=0),
    type='OptimWrapper')
param_scheduler = [
    dict(
        begin=0, by_epoch=False, end=1000, start_factor=1e-05,
        type='LinearLR'),
    dict(
        T_max=105,
        begin=105,
        by_epoch=True,
        convert_to_iter_based=True,
        end=210,
        eta_min=0.0002,
        type='CosineAnnealingLR'),
]
randomness = dict(seed=21)
resume = False
stage2_num_epochs = 30
test_cfg = dict()
test_dataloader = dict(
    batch_size=64,
    dataset=dict(
        ann_file=
        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/annotations/person_keypoints_val2017.json',
        data_mode='topdown',
        data_prefix=dict(
            img=
            '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/images/val2017/'
        ),
        data_root=
        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/',
        pipeline=[
            dict(backend_args=dict(backend='local'), type='LoadImage'),
            dict(type='GetBBoxCenterScale'),
            dict(input_size=(
                192,
                256,
            ), type='TopdownAffine', use_udp=True),
            dict(type='PackPoseInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=10,
    persistent_workers=True,
    sampler=dict(round_up=False, shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    ann_file=
    '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose//annotations/person_keypoints_val2017.json',
    type='CocoMetric')
train_cfg = dict(by_epoch=True, max_epochs=210, val_interval=10)
train_dataloader = dict(
    batch_size=256,
    dataset=dict(
        datasets=[
            dict(
                dataset=dict(
                    ann_file=
                    '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/annotations/person_keypoints_train2017.json',
                    data_mode='topdown',
                    data_prefix=dict(
                        img=
                        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/images/train2017/'
                    ),
                    data_root=
                    '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/',
                    pipeline=[
                        dict(
                            mapping=[
                                (
                                    0,
                                    0,
                                ),
                                (
                                    1,
                                    1,
                                ),
                                (
                                    2,
                                    2,
                                ),
                                (
                                    3,
                                    3,
                                ),
                                (
                                    4,
                                    4,
                                ),
                                (
                                    5,
                                    5,
                                ),
                                (
                                    6,
                                    6,
                                ),
                                (
                                    7,
                                    7,
                                ),
                                (
                                    8,
                                    8,
                                ),
                                (
                                    9,
                                    9,
                                ),
                                (
                                    10,
                                    10,
                                ),
                                (
                                    11,
                                    11,
                                ),
                                (
                                    12,
                                    12,
                                ),
                                (
                                    13,
                                    13,
                                ),
                                (
                                    14,
                                    14,
                                ),
                                (
                                    15,
                                    15,
                                ),
                                (
                                    16,
                                    16,
                                ),
                            ],
                            num_keypoints=19,
                            type='KeypointConverter'),
                    ],
                    type='CocoDataset'),
                times=3,
                type='RepeatDataset'),
        ],
        metainfo=dict(from_file='configs/_base_/datasets/coco.py'),
        pipeline=[
            dict(backend_args=dict(backend='local'), type='LoadImage'),
            dict(type='GetBBoxCenterScale'),
            dict(direction='horizontal', type='RandomFlip'),
            dict(type='RandomHalfBody'),
            dict(
                rotate_factor=80,
                scale_factor=[
                    0.6,
                    1.4,
                ],
                type='RandomBBoxTransform'),
            dict(input_size=(
                192,
                256,
            ), type='TopdownAffine', use_udp=True),
            dict(type='mmdet.YOLOXHSVRandomAug'),
            dict(
                transforms=[
                    dict(p=0.1, type='Blur'),
                    dict(p=0.1, type='MedianBlur'),
                    dict(
                        max_height=0.4,
                        max_holes=1,
                        max_width=0.4,
                        min_height=0.2,
                        min_holes=1,
                        min_width=0.2,
                        p=1.0,
                        type='CoarseDropout'),
                ],
                type='Albumentation'),
            dict(
                encoder=dict(
                    heatmap_size=(
                        48,
                        64,
                    ),
                    input_size=(
                        192,
                        256,
                    ),
                    sigma=2,
                    type='UDPHeatmap'),
                type='GenerateTarget'),
            dict(type='PackPoseInputs'),
        ],
        test_mode=False,
        type='CombinedDataset'),
    num_workers=10,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(backend_args=dict(backend='local'), type='LoadImage'),
    dict(type='GetBBoxCenterScale'),
    dict(direction='horizontal', type='RandomFlip'),
    dict(type='RandomHalfBody'),
    dict(
        rotate_factor=80,
        scale_factor=[
            0.6,
            1.4,
        ],
        type='RandomBBoxTransform'),
    dict(input_size=(
        192,
        256,
    ), type='TopdownAffine', use_udp=True),
    dict(type='mmdet.YOLOXHSVRandomAug'),
    dict(
        transforms=[
            dict(p=0.1, type='Blur'),
            dict(p=0.1, type='MedianBlur'),
            dict(
                max_height=0.4,
                max_holes=1,
                max_width=0.4,
                min_height=0.2,
                min_holes=1,
                min_width=0.2,
                p=1.0,
                type='CoarseDropout'),
        ],
        type='Albumentation'),
    dict(
        encoder=dict(
            heatmap_size=(
                48,
                64,
            ),
            input_size=(
                192,
                256,
            ),
            sigma=2,
            type='UDPHeatmap'),
        type='GenerateTarget'),
    dict(type='PackPoseInputs'),
]
train_pipeline_stage2 = [
    dict(backend_args=dict(backend='local'), type='LoadImage'),
    dict(type='GetBBoxCenterScale'),
    dict(direction='horizontal', type='RandomFlip'),
    dict(type='RandomHalfBody'),
    dict(
        rotate_factor=60,
        scale_factor=[
            0.75,
            1.25,
        ],
        shift_factor=0.0,
        type='RandomBBoxTransform'),
    dict(input_size=(
        192,
        256,
    ), type='TopdownAffine', use_udp=True),
    dict(type='mmdet.YOLOXHSVRandomAug'),
    dict(
        transforms=[
            dict(p=0.1, type='Blur'),
            dict(p=0.1, type='MedianBlur'),
            dict(
                max_height=0.4,
                max_holes=1,
                max_width=0.4,
                min_height=0.2,
                min_holes=1,
                min_width=0.2,
                p=0.5,
                type='CoarseDropout'),
        ],
        type='Albumentation'),
    dict(
        encoder=dict(
            heatmap_size=(
                48,
                64,
            ),
            input_size=(
                192,
                256,
            ),
            sigma=2,
            type='UDPHeatmap'),
        type='GenerateTarget'),
    dict(type='PackPoseInputs'),
]
val_cfg = dict()
val_dataloader = dict(
    batch_size=64,
    dataset=dict(
        ann_file=
        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/annotations/person_keypoints_val2017.json',
        data_mode='topdown',
        data_prefix=dict(
            img=
            '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/images/val2017/'
        ),
        data_root=
        '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose/',
        pipeline=[
            dict(backend_args=dict(backend='local'), type='LoadImage'),
            dict(type='GetBBoxCenterScale'),
            dict(input_size=(
                192,
                256,
            ), type='TopdownAffine', use_udp=True),
            dict(type='PackPoseInputs'),
        ],
        test_mode=True,
        type='CocoDataset'),
    drop_last=False,
    num_workers=10,
    persistent_workers=True,
    sampler=dict(round_up=False, shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    ann_file=
    '/home/siton01/yolov8-20230924/yolov8-main/ultralytics/yolo/cfg/coco2017labels-pose/coco-pose//annotations/person_keypoints_val2017.json',
    type='CocoMetric')
val_pipeline = [
    dict(backend_args=dict(backend='local'), type='LoadImage'),
    dict(type='GetBBoxCenterScale'),
    dict(input_size=(
        192,
        256,
    ), type='TopdownAffine', use_udp=True),
    dict(type='PackPoseInputs'),
]
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='PoseLocalVisualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = './work_dirs/cspnext-l_udp_8xb256-210e_aic-coco-256x192'
