import nptdms
import pandas


def read_tdms(
        tdms_path,
        tdms_group_name):
    """Load measurements from TDMS file.
    
    Load measurements and channel metadata from the input TDMS
    file.
    """
    with nptdms.TdmsFile.open(tdms_path) as tdms_file:
        # Check the TDMS group is inside the input TDMS file.
        found = False
        for group in tdms_file.groups():
            if tdms_group_name == group.name:
                found = True
        if not found:
            raise ValueError(f"TDMS group `{tdms_group_name}` not found")

        # Load measurements.
        data = tdms_file[tdms_group_name].as_dataframe(
            time_index=True,
            absolute_time=False
        )
            
        # Load channel metadata.
        meta = {}
        for channel in tdms_file[tdms_group_name].channels():
            for key, value in channel.properties.items():
                if key not in meta:
                    meta[key] = []
                meta[key].append(value)
        meta = pandas.DataFrame(meta)

    return data, meta
