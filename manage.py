
import os
import json
from src.exporter import Exporter
from src.helper import current_milli_time, slack_ping

if __name__ == "__main__":

    try:
        start = current_milli_time() # Start time

        # Start Automation Process
        exporter = Exporter()
        exporter.create_result_dir()
        exporter.run_test()

        # Push to gateway report
        total, success_apis, failed_apis = exporter.push_report()

        # Clean result cache
        exporter.clean_results()

        end = current_milli_time() # End time

        time_taken = end - start

        # Ping slack
        slack_ping(total, len(success_apis), len(failed_apis), time_taken)

        if len(failed_apis) > 0:
            print("Failed:\n")
            for err in failed_apis:
                print(err)
        else:
            os.system("mkdir succeed")
            f = open("succeed/api.txt", "a")
            f.write(json.dumps(success_apis))
            f.close()
            print("Well done !")
    
    except Exception as e:
        raise Exception("Not working !", e)
