export const getBackgroundColor = (data: any) => {
    var color = "linear-gradient(135deg, #D3D3D3, #A9A9A9)"
    // console.log(data.name, data.isLegendary)
    if(data.isMythical == true) {
        color = "linear-gradient(to right, #8e2de2, #4a00e0)"
    }
    else if(data.isLegendary == true){
        color = "linear-gradient(135deg, #fdc830, #f37335)"
    }

    return color
};
