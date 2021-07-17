data = list(map(int, input().split()))
imageHeight = data[0]
imageWidth = data[1]
kernelHeight = data[2]
kernelWidth = data[3]

imageValues = []
for _ in range(imageHeight):
    imageValues.extend(input().split())

kernelValues = []
for _ in range(kernelHeight):
    kernelValues.extend(input().split())

imageValues = list(map(int, imageValues))
kernelValues = list(map(int, kernelValues))

resultingImageHeight = imageHeight - kernelHeight + 1
resultingImageWidth = imageWidth - kernelWidth + 1
for resultingImageHeightIndex in range(resultingImageHeight):
    resultingImageRow = []
    for resultingImageWidthIndex in range(resultingImageWidth):
        entry = 0
        for kernelHeightIndex in range(kernelHeight):
            for kernelWidthIndex in range(kernelWidth):
                imageHeightIndex = imageWidth * (resultingImageHeightIndex + kernelHeightIndex)
                imageWidthIndex = resultingImageWidthIndex + kernelWidthIndex
                imageIndex = imageHeightIndex + imageWidthIndex
                imageValue = imageValues[imageIndex]

                kernelIndex = kernelWidth * (kernelHeight - kernelHeightIndex - 1) + (kernelWidth - kernelWidthIndex - 1)
                kernelValue = kernelValues[kernelIndex]
                entry += imageValue * kernelValue

        resultingImageRow.append(str(entry))

    print(" ".join(resultingImageRow))
