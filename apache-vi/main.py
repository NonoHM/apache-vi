import av_parser as pa
import diagram as dg
import html_creator as html
import argparse
import webbrowser

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', help='Input log file')
parser.add_argument('--output-dir', help='Output directory')
args = parser.parse_args()

input_file = args.input_file
output_dir = args.output_dir

def render():
    print('The statistics are being rendered... ')
    log_length = pa.log_length(input_file)
    nav_dict = pa.browser_number(input_file)
    date_dict = pa.connection_number(input_file)
    dict_month = pa.connection_month(date_dict, True)
    dict_week = pa.connection_week(date_dict)
    dg.make_all(dict_week, dict_month, nav_dict, output_dir)
    html.html_creator(log_length, output_dir)
    webbrowser.open(f'{output_dir}/index.html')
    print(f"Finished ! The website has been made in {output_dir}")

def main():
    render()

if __name__ == "__main__":
    main()
