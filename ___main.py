import matplotlib.pyplot as plt
import pathlib
from segysak.segy import get_segy_texthead
from segysak.segy import segy_loader, well_known_byte_locs


V3D_path = pathlib.Path("seismicdataset/mig.sgy")
print("2D", V3D_path, V3D_path.exists())

get_segy_texthead(V3D_path)

V3D = segy_loader(V3D_path, iline=189, xline=193, cdpx=73, cdpy=77, vert_domain="TWT")

fig, ax1 = plt.subplots(ncols=1, figsize=(15, 8))
iline_sel = 10093
V3D.data.transpose("twt", "iline", "xline", transpose_coords=True).sel(
    iline=iline_sel
).plot(yincrease=False, cmap="seismic_r")
plt.grid("grey")
plt.ylabel("TWT")
plt.xlabel("XLINE")