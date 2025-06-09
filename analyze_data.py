import pandas as pd
import argparse


def analyze(path):
    """Load a CSV file and print summary statistics."""
    df = pd.read_csv(path)
    print("Summary statistics:")
    print(df.describe())


def main():
    parser = argparse.ArgumentParser(description="Analyze a CSV file")
    parser.add_argument("path", help="Path to CSV file")
    args = parser.parse_args()
    analyze(args.path)


if __name__ == "__main__":
    main()
