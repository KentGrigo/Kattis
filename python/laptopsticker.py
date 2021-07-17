margin = 1
computerWidth, computerHeight, stickerWidth, stickerHeight = list(map(int, input().split()))
willFitHorizontally = margin + stickerWidth + margin <= computerWidth
willFitVertically = margin + stickerHeight + margin <= computerHeight
willFit = willFitHorizontally and willFitVertically
if willFit:
    print(1)
else:
    print(0)
