import argparse
import warnings

# import yaml
from ruamel.yaml import YAML

yaml = YAML(typ="safe")

from utils.data import get_data
from utils.result import generate_result
from utils.test import test_model
from utils.train import train_model

warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Self Attention Based HAR Model Training')

    parser.add_argument('--train', action='store_true', default=False, help='Training Mode')
    parser.add_argument('--test', action='store_true', default=False, help='Testing Mode')
    parser.add_argument('--epochs', default=100, type=int, help='Number of Epochs for Training')
    parser.add_argument('--dataset', default='pamap2', type=str, help='Name of Dataset for Model Training')
    parser.add_argument('--rotate', default=False, type=bool, help='3D rotation-augmentation of Training Dataset')
    parser.add_argument('--RANDOM_SEED', default=42, type=int)

    args = parser.parse_args()

    model_config_file = open('configs/model.yaml', mode='r')
    model_cfg = yaml.load(model_config_file)

    train_x, train_y, val_x, val_y, test_x, test_y = get_data(args)

    if args.train:
        print('\n[MODEL TRAINING]')
        train_model(dataset=args.dataset,
                    model_config=model_cfg,
                    train_x=train_x, train_y=train_y,
                    val_x=val_x, val_y=val_y,
                    epochs=args.epochs)

    if args.test:
        print('\n[MODEL INFERENCE]')
        pred = test_model(dataset=args.dataset, model_config=model_cfg, test_x=test_x)
        generate_result(dataset=args.dataset, ground_truth=test_y, prediction=pred)
